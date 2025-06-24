from transformers import pipeline

# Load a text generation model
generator = pipeline("text-generation", model="gpt2")

# Input
prompt = input("Enter a prompt: ")

# Generate text
output = generator(prompt, max_length=100, num_return_sequences=1)

# Show result
print("\nGenerated text:\n")
print(output[0]["generated_text"])
