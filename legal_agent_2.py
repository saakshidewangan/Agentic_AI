import fitz  # PyMuPDF for reading PDFs
import ollama  # Ollama for LLM processing
from phi.model.groq import Groq

def extract_text_from_pdf(pdf_path):
    """Extracts text from a given PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text() + "\n"
    return text.strip()

class LegalAgent:
    def __init__(self, model="llama3"):
        """Initialize the legal agent with an LLM model."""
        self.model = model

    def process_pdf(self, pdf_path):
        """Reads the PDF and stores its content."""
        self.legal_text = extract_text_from_pdf(pdf_path)
        print("✅ PDF loaded successfully!")

    def answer_question(self, question):
        """Answers questions based on the PDF content."""
        if not hasattr(self, 'legal_text') or not self.legal_text:
            return "Error: No PDF content loaded. Please upload a PDF first."

        prompt = f"""You are a legal assistant. The following document has been provided:
        {self.legal_text}
        
        Question: {question}
        Answer:"""

        response = ollama.chat(model=self.model, messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]

# Usage Example
if __name__ == "__main__":
    agent = LegalAgent()

    # Load a PDF file (replace with your actual file path)
    pdf_path = "C:\\Users\\KIIT\\Desktop\\RESUME ELEMENTS\\Saakshi_Dewangan_Resume_Campus(2).pdf"
    agent.process_pdf(pdf_path)

    # Ask a question about the document
    question = input("Ask a question about the legal document: ")
    answer = agent.answer_question(question)
    print("\n💡 Answer:", answer)
