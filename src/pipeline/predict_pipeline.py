'''
b) train_pipeline.py
Purpose

Runs the entire training process.

Instead of writing

Read Data

↓

Clean Data

↓

Train Model

↓

Save Model

inside one notebook, this file calls each component.

Example:

ingestion = DataIngestion()

transformation = DataTransformation()

trainer = ModelTrainer()

Simple meaning:

Runs the complete training workflow.'''