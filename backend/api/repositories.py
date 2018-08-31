from . import sentence_generator
from uuid import uuid4

class SentenceRepository():
    def get(self, count=10):
        sentences = sentence_generator.generate(count)
        return {str(uuid4()): sentence for sentence in sentences}
