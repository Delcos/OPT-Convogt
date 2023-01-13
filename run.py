from transformers import AutoTokenizer, OPTForCausalLM

class GPTGenerator:
    def __init__(self, model_name_or_path: str):
        self.tokenizer = AutoTokenizer.from_pretrained('facebook/opt-2.7b')
        self.model = OPTForCausalLM.from_pretrained(
            model_name_or_path
        ).eval()

    def generate(self, prompt: str, max_length: int, count: int):
        output = {}

        input_ids = self.tokenizer.encode(
            prompt,
            return_tensors='pt'
        ).repeat(count, 1)

        output = self.model.generate(
            input_ids=input_ids,
            do_sample=True,
            max_new_tokens=max_length,
            temperature=0.5,
            top_p=0.9,
            typical_p=0.98,
            repetition_penalty=1.05,
            pad_token_id=self.tokenizer.eos_token_id,
            eos_token_id=198,
        )[:, input_ids.shape[1]:]

        output = self.tokenizer.batch_decode(
            output,
            skip_special_tokens=True
        )

        return output

generator = GPTGenerator("models/opt-350/")

while True:
    prompt = input("Please enter your input: ")
    if prompt == "exit":
        break
    print(generator.generate(prompt, 40, 1))

