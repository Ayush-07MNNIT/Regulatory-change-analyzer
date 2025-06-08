AI-Powered Regulatory Change Analyzer

This project is a full-stack AI-powered tool designed to detect and analyze changes between versions of regulatory documents. It was developed to automate the tedious and error-prone task of regulatory compliance change tracking.


Some Features are 

  Upload two versions of a regulatory document (in .txt format)
  Detect Added, Deleted, and Modified sentences
  Use a local LLM (I am using TinyLlama via Ollama over phi3 due storage Gpu issue) to:
   - Summarize the change
   - Categorize its type
   - Predict its potential impact
  View changes in a clean, interactive Streamlit UI
  Gracefully handle invalid LLM responses with regex fallback as it was showing parsing error.


  Tech Stack

- Python
- Streamlit ( For Frontend UI)
- difflib (Sentence-level comparison)
- Ollama + TinyLlama (Open-source local LLM)
- Regex-based JSON parser fallback

 Project Structure


regulatory_diff_ai_app/
── app.py                  # Streamlit app used for frontend
── change_detector.py     # Sentence diff logic
── llm_analyzer.py        # LLM query + JSON fallback handling
── requirements.txt       # Generally used Dependencies
── sample_data/
    ── text_v1.txt        # Old version
    ── text_v2.txt        # New version


For  Installation and smooth run

 Pull a compatible model with Ollama

    give command ollama pull tinyllama in terminal of vscode 
    
    
 streamlit run app.py for making it run


 Notes

- Works offline with open-source models
- Best used with short .txt documents
- Only Added and Modified content is analyzed
