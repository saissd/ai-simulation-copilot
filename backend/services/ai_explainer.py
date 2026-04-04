import os
api_key = os.getenv("OPENAI_API_KEY")
def generate_insight(summary_text):
    """
    Generates simple AI-like insight (no OpenAI needed)
    """

    if not summary_text:
        return "No insight available."

    # Simple human-style explanation
    return (
        f"Based on the simulation, {summary_text.lower()} "
        "Regions with higher scalar values may indicate areas of higher intensity or activity."
    )


def answer_question_about_simulation(summary_text, question):
    q = question.lower()

    if "highest" in q or "max" in q:
        return "The highest values likely indicate hotspots in the simulation."

    if "temperature" in q:
        return "Temperature variations suggest different intensity zones in the dataset."

    if "pressure" in q:
        return "Pressure distribution shows areas of concentration and spread."

    if "hotspot" in q:
        return "Hotspots are regions with higher scalar values such as temperature or pressure."

    return f"Based on the simulation: {summary_text}"