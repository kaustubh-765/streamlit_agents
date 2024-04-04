from pydantic import BaseModel

class ContentPromptParameter(BaseModel):
    """Pydantic model defining prompt parameters."""

    topic: str
    paragraphs: int = 2
    lines_per_paragraph: int = 4
    sources: int = 5
    youtube_links: int = 5

class YoutubePromptParameter(BaseModel):
    """Pydantic model defining prompt parameters."""

    transcript: str
    video_id: str

class YoutubeChaptersParameter(BaseModel):
    """Pydantic model defining prompt parameters."""

    video_id: str
    chapters: str
    
class AssessmentPromptParameter(BaseModel):
    """
        `Structure for the Parameters for the Prompt`

        Parameters:
            language_type (str): Name of the programming language to practice.
            question_level (str): Difficulty level of the question [Easy, Medium, High]. 
            topic (str): Topic related to the language currently practicing.
            summary (str): It contains the summary of the topic related to the language.
    """
    language_type :str
    question_level : str
    topic: str
    summary: str