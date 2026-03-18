import argparse
import csv
from collections import Counter
from transformers import pipeline


# ---------- Load models ----------
rewriter = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    framework="pt",
    device=-1
)

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt",
    device=-1
)


# ---------- Helpers ----------
def count_tokens(text):
    return len(text.split())


def validate(text):
    words = text.strip().split()

    if not text.endswith("."):
        return False, "no period"
    if len(words) < 8:
        return False, "too short"
    if len(words) > 24:
        return False, "too long"
    if text.count(".") > 1:
        return False, ">1 sentence"

    return True, ""


def clean_output(text):
    return text.split(".")[0].strip() + "."


def generate(prompt, mode):
    if mode == "beam":
        return rewriter(
            prompt,
            max_new_tokens=40,
            min_length=12,
            num_beams=4,
            do_sample=False
        )[0]["generated_text"]

    else:  # sampling
        return rewriter(
            prompt,
            max_new_tokens=40,
            min_length=12,
            do_sample=True,
            temperature=0.9,
            top_p=0.95
        )[0]["generated_text"]


def neutralize(label, score, band=0.1):
    if abs(score - 0.5) <= band:
        return "NEUTRAL"
    return label


# ---------- Main ----------
def process(infile, save_csv=False):
    with open(infile, "r", encoding="utf-8") as f:
        inputs = [line.strip() for line in f if line.strip()]

    rows = []

    beam_pass = 0
    sampling_pass = 0
    retry_fixed = 0

    lengths = []
    raw_sentiment = []
    adjusted_sentiment = []

    print("\n--- Sample Outputs ---\n")

    for i, text in enumerate(inputs):
        prompt = (
            "Rewrite the following sentence in simple English. "
            "Use only ONE sentence. Use 8 to 24 words. End with a period.\n\n"
            f"{text}"
        )

        # ---- Beam ----
        beam_out = clean_output(generate(prompt, "beam"))
        beam_valid, beam_note = validate(beam_out)

        # ---- Sampling ----
        sampling_out = clean_output(generate(prompt, "sampling"))
        sampling_valid, sampling_note = validate(sampling_out)

        # ---- Retry logic ----
        used_retry = False
        if beam_valid:
            final_out = beam_out
            beam_pass += 1
        else:
            final_out = sampling_out
            used_retry = True
            if sampling_valid:
                retry_fixed += 1

        if sampling_valid:
            sampling_pass += 1

        lengths.append(count_tokens(final_out))

        # ---- Sentiment ----
        sent = sentiment_model(text)[0]
        raw_label = sent["label"]
        score = sent["score"]
        adj_label = neutralize(raw_label, score)

        raw_sentiment.append(raw_label)
        adjusted_sentiment.append(adj_label)

        rows.append({
            "input": text,
            "beam_output": beam_out,
            "sampling_output": sampling_out,
            "final_output": final_out,
            "beam_valid": beam_valid,
            "sampling_valid": sampling_valid,
            "retry_used": used_retry
        })

        # Print first 3 examples
        if i < 3:
            print(f"Input: {text}")
            print(f"Beam: {beam_out} ({beam_valid})")
            print(f"Sampling: {sampling_out} ({sampling_valid})")
            print(f"Final: {final_out} (retry={used_retry})\n")

    total = len(inputs)

    # ---------- Metrics ----------
    print("\n--- Final Metrics ---")

    print(f"Beam pass rate: {beam_pass/total*100:.2f}%")
    print(f"Sampling pass rate: {sampling_pass/total*100:.2f}%")
    print(f"Retry fixed rate: {retry_fixed/total*100:.2f}%")

    print(f"\nAverage output length: {sum(lengths)/len(lengths):.2f} words")

    print("\nSentiment distribution (raw):")
    print(dict(Counter(raw_sentiment)))

    print("\nSentiment distribution (after neutral band):")
    print(dict(Counter(adjusted_sentiment)))

    # ---------- Optional CSV ----------
    if save_csv:
        with open("task3_results.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)

        print("\nSaved: task3_results.csv")


# ---------- CLI ----------
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", required=True)
    parser.add_argument("--save_csv", action="store_true")

    args = parser.parse_args()

    process(args.infile, args.save_csv)