from transformers import pipeline

pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    framework="pt",
    device=-1
)

out = pipe(
    "Rewrite in simple English: The process was exceedingly complicated and difficult to follow.",
    max_new_tokens=40,
    do_sample=False
)

print(out)