import streamlit as st
import json

from module_extractor import run_pipeline

st.set_page_config(page_title="Pulse – Module Extraction AI Agent", layout="wide")

st.title("📘 Pulse – Module Extraction AI Agent")
st.markdown("Extract product modules and submodules from documentation automatically.")

urls_input = st.text_area(
    "Enter documentation URLs (one per line)",
    placeholder="https://help.zluri.com/\nhttps://wordpress.org/documentation/"
)

if st.button("Run Extraction"):
    if not urls_input.strip():
        st.warning("Please enter at least one URL.")
    else:
        urls = urls_input.splitlines()

        with st.spinner("Processing documentation..."):
            try:
                result = run_pipeline(urls)

                st.success("Extraction completed successfully!")

                st.subheader("📄 Structured Output")
                st.json(result)

                st.download_button(
                    label="Download JSON",
                    data=json.dumps(result, indent=2),
                    file_name="modules_output.json",
                    mime="application/json"
                )

            except Exception as e:
                st.error(str(e))
