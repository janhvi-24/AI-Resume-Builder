from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the model and tokenizer
model_name = "EleutherAI/gpt-neo-125M"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def suggest_improvements(section, content):
    if not content.strip():
        return "No content provided to improve."
    try:
        prompt = f"Improve the following {section} section of a resume:\n{content}"
        inputs = tokenizer(prompt, return_tensors="pt", max_length=512, truncation=True)
        outputs = model.generate(inputs["input_ids"], max_length=150, num_return_sequences=1)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error generating suggestions: {e}"
