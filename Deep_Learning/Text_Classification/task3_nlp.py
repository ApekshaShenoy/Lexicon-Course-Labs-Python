import argparse
from collections import Counter
from transformers import pipeline

rewriter = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    framework="pt",
    device=-1
)

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6",
    framework="pt",
    device=-1
)

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt",
    device=-1
)

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


def generate(prompt, mode, task="rewrite"):
    if mode == "beam":
        return rewriter(
            prompt,
            max_new_tokens=40,
            min_length=12,
            num_beams=4,
            do_sample=False
        )[0]["generated_text"]

    elif mode == "sampling":
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

def process(infile):
    with open(infile, "r", encoding="utf-8") as f:
        inputs = [line.strip() for line in f if line.strip()]

    results = []

    beam_pass = 0
    sampling_pass = 0
    retry_success = 0

    lengths = []

    raw_sentiment = []
    adjusted_sentiment = []

    for text in inputs:
        prompt = (
            "Rewrite the following sentence in simple English. "
            "Use only ONE sentence. Use 8 to 24 words. End with a period.\n\n"
            f"{text}"
        )

       
        beam_out = clean_output(generate(prompt, "beam"))
        beam_valid, _ = validate(beam_out)

        if beam_valid:
            beam_pass += 1
            final_out = beam_out
        else:
           
            retry_out = clean_output(generate(prompt, "sampling"))
            retry_valid, _ = validate(retry_out)

            if retry_valid:
                retry_success += 1
                final_out = retry_out
            else:
                final_out = retry_out

        
        sampling_out = clean_output(generate(prompt, "sampling"))
        sampling_valid, _ = validate(sampling_out)
        if sampling_valid:
            sampling_pass += 1

        lengths.append(count_tokens(final_out))

        sent = sentiment_model(text)[0]
        raw_label = sent["label"]
        score = sent["score"]

        adj_label = neutralize(raw_label, score)

        raw_sentiment.append(raw_label)
        adjusted_sentiment.append(adj_label)

        results.append({
            "input": text,
            "output": final_out
        })

    total = len(inputs)

    print("\n--- Final Metrics ---")

    print(f"Beam pass rate: {beam_pass/total*100:.2f}%")
    print(f"Sampling pass rate: {sampling_pass/total*100:.2f}%")
    print(f"Retry success rate: {retry_success/total*100:.2f}%")

    print(f"\nAverage output length: {sum(lengths)/len(lengths):.2f} words")

    print("\nSentiment distribution (raw):")
    print(dict(Counter(raw_sentiment)))

    print("\nSentiment distribution (after neutral band):")
    print(dict(Counter(adjusted_sentiment)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", required=True, help="Input file")

    args = parser.parse_args()

    process(args.infile)