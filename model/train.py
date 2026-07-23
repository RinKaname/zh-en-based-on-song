import os
from datasets import load_dataset
from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    DataCollatorForSeq2Seq,
    Seq2SeqTrainer,
    Seq2SeqTrainingArguments
)

def main():
    # 1. Load the jsonl datasets we created
    # Ensure paths are correct relative to where the script is executed
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_files = [
        os.path.join(script_dir, "../translation_dataset.jsonl"),
        os.path.join(script_dir, "../lyria3_dataset.jsonl")
    ]

    # Verify files exist
    for f in data_files:
        if not os.path.exists(f):
            raise FileNotFoundError(f"Dataset file not found: {f}")

    # Use Hugging Face datasets library to load JSON Lines files directly
    dataset = load_dataset("json", data_files=data_files)

    # Split into train and test sets
    dataset = dataset["train"].train_test_split(test_size=0.1)

    # 2. Load Tokenizer & Model
    model_name = "Helsinki-NLP/opus-mt-zh-en"
    print(f"Loading model and tokenizer: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    # 3. Preprocessing function for tokenization
    def preprocess_function(examples):
        inputs = examples["source"]
        targets = examples["target"]

        # Tokenize inputs (source language)
        model_inputs = tokenizer(inputs, max_length=128, truncation=True)

        # Tokenize targets (target language)
        labels = tokenizer(text_target=targets, max_length=128, truncation=True)
        model_inputs["labels"] = labels["input_ids"]

        return model_inputs

    print("Tokenizing datasets...")
    tokenized_dataset = dataset.map(preprocess_function, batched=True, desc="Running tokenizer on dataset")

    # 4. Data collator for sequence-to-sequence tasks
    data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

    # 5. Training Arguments
    training_args = Seq2SeqTrainingArguments(
        output_dir=os.path.join(script_dir, "opus_zh_en_finetuned"),
        eval_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=4,
        per_device_eval_batch_size=4,
        weight_decay=0.01,
        save_total_limit=3,
        num_train_epochs=5,
        predict_with_generate=True,
        fp16=True, # Note: Set to False if running on CPU or unsupported hardware
        logging_steps=5,
        report_to="none" # Prevents warnings if Weights & Biases isn't installed
    )

    # 6. Initialize Trainer
    trainer = Seq2SeqTrainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["test"],
        processing_class=tokenizer,
        data_collator=data_collator,
    )

    # 7. Fine-tune the model
    print("Starting training...")
    trainer.train()

    # 8. Save final model
    final_dir = os.path.join(script_dir, "opus_zh_en_finetuned_final")
    print(f"Training complete! Saving model to {final_dir}...")
    trainer.save_model(final_dir)

if __name__ == "__main__":
    main()
