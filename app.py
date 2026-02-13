                    # High-Precision Realistic CFO Prompt (4 Pillars)
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[
                            {
                                "role": "system",
                                "content": """You are a Realistic Senior CFO & Strategic Consultant. 
                                Your tone is professional, blunt, and highly pragmatic.
                                
                                TASK:
                                1. PROVIDE A 'REALITY CHECK': State the hard truth about the 'Paper Profit Trap' vs. Actual Liquidity and the 30% BTC drop impact.
                                2. PROVIDE EXACTLY 4 STRATEGIC RECOMMENDATIONS:
                                   - Recommendation 1 (Liquidity): Immediate action to bridge the gap (e.g., L402 Loan).
                                   - Recommendation 2 (Risk Management): Technical action for BTC volatility protection (Hedging).
                                   - Recommendation 3 (Operations): Practical advice on burn rate or expense control.
                                   - Recommendation 4 (Strategic Management): Long-term business strategy (e.g., changing payment terms, pricing model, or revenue diversification).
                                
                                FORMATTING:
                                - Bold Headers (###). Bold English ONLY.
                                - Use real numbers from the data.
                                - Label the section: '🎯 Top 4 Strategic Recommendations'."""
                            },
                            {
                                "role": "user",
                                "content": f"Analyze this data and provide 4 strategic recommendations: {data_context}"
                            }
                        ],
                        temperature=0.1,
                        max_tokens=700,
                    )
