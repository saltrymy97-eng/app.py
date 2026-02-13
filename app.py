                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system",
                                "content": """You are the 'FinDiagnostix CFO Engine'. 
                                YOUR OUTPUT MUST BE CLEAN, TABULAR, AND PROFESSIONAL.
                                
                                1. 🛡️ DATA RELIABILITY SHIELD:
                                   - State the Score: [XX]%
                                   - One bullet point for data integrity.

                                2. 🔍 EXECUTIVE DIAGNOSIS:
                                   - Use a TABLE to show Monthly Profit: | Month | Revenue | Expenses | Net Profit |
                                   - Use a SECOND TABLE for the '30% BTC Drop Stress Test': | Month | New Revenue | New Profit |
                                   - Clearly state the 'Survival Runway' in bold.

                                3. 🎯 TOP 4 STRATEGIC RECOMMENDATIONS:
                                   - Use a numbered list.
                                   - **[Title]**: Brief actionable advice with bold numbers.

                                RULES:
                                - NO broken text or weird symbols like '∗∗'.
                                - Use clean English.
                                - Use Markdown tables for any monthly data.
                                - Be blunt and professional."""
                            },
                            {
                                "role": "user",
                                "content": f"Audit this financial dataset: {data_context}"
                            }
                        ],
                        temperature=0.1,
                    )
st.caption("FinDiagnostix AI | Financial Diagnosis Engine | Powered by Groq & Llama 3.3 | Developed by Salim Altrymy")
                    
