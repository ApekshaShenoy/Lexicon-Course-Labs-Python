from transformers import pipeline

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

sentence = input("Enter one sentence: ")

prompt = (
    "Rewrite the following sentence in simple English. "
    "Use only ONE sentence. "
    "Use between 8 and 24 words. "
    "Do not split into multiple sentences. "
    "End with a period.\n\n"
    f"{sentence}"
)

result = rewriter(
    prompt,
    max_new_tokens=40,
    min_length=12,
    num_beams=4,
    early_stopping=True,
    do_sample=False
)[0]["generated_text"]

print("\nRewrite:", result)

ok, note = validate(result)
if not ok:
    print("constraint not satisfied:", note)


print("\nEnter 3 sentences for sentiment:")
sentences = [input(f"{i+1}: ") for i in range(3)]

results = sentiment_model(sentences)

print("\nSentiment:")
for s, r in zip(sentences, results):
    print(f"{s} -> {r['label']} ({r['score']:.4f})")

print(
    "\nNote: This model has only POSITIVE and NEGATIVE labels. "
    "There is no Neutral class, so uncertain cases are forced into one of the two."
)