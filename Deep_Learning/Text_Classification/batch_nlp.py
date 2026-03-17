import argparse
import csv
from transformers import pipeline


generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
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


def generate(prompt, mode):
    if mode == "beam":
        return generator(
            prompt,
            max_new_tokens=40,
            min_length=12,
            num_beams=4,
            early_stopping=True,
            do_sample=False
        )[0]["generated_text"]

    elif mode == "sampling":
        return generator(
            prompt,
            max_new_tokens=40,
            min_length=12,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )[0]["generated_text"]


def process(infile, outfile):
    rows = []

    with open(infile, "r", encoding="utf-8") as f:
        inputs = [line.strip() for line in f if line.strip()]

    for text in inputs:
        prompt = (
            "Rewrite the following sentence in simple English. "
            "Use only ONE sentence. "
            "Use between 8 and 24 words. "
            "End with a period.\n\n"
            f"{text}"
        )

        for mode in ["beam", "sampling"]:
            output = generate(prompt, mode)
            output = clean_output(output)

            valid, note = validate(output)

            rows.append({
                "input": text,
                "output": output,
                "decoding": mode,
                "tokens_out": count_tokens(output),
                "constraint_passed": valid,
                "notes": note
            })

    with open(outfile, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "input",
                "output",
                "decoding",
                "tokens_out",
                "constraint_passed",
                "notes"
            ]
        )
        writer.writeheader()
        writer.writerows(rows)

  
    print("\n--- Mini Report ---")

    for mode in ["beam", "sampling"]:
        subset = [r for r in rows if r["decoding"] == mode]

        passed = sum(r["constraint_passed"] for r in subset)
        total = len(subset)
        avg_tokens = sum(r["tokens_out"] for r in subset) / total

        print(f"\nMode: {mode}")
        print(f"Pass rate: {passed/total*100:.2f}%")
        print(f"Average tokens_out: {avg_tokens:.2f}")

        if mode == "beam":
            print("Beam search produces more consistent and controlled outputs.")
        else:
            print("Sampling is more flexible but less reliable for constraints.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", required=True, help="Input .txt file")
    parser.add_argument("--outfile", default="results.csv", help="Output CSV file")

    args = parser.parse_args()

    process(args.infile, args.outfile)