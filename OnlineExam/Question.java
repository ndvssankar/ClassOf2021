

public class Question {

    private String questionText;
    private String[] options;
    private String[] correctOption;
    private int score;
    private int level;

    public Question() {
    }

    public Question(String questionText, String[] options, String[] correctOption, int score, int level) {
        this.questionText = questionText;
        this.options = options;
        this.correctOption = correctOption;
        this.score = score;
        this.level = level;
    }

    public String getQuestionText() {
        return this.questionText;
    }

    public void setQuestionText(String questionText) {
        this.questionText = questionText;
    }

    public String[] getOptions() {
        return this.options;
    }

    public void setOptions(String[] options) {
        this.options = options;
    }

    public String[] getCorrectOption() {
        return this.correctOption;
    }

    public void setCorrectOption(String[] correctOption) {
        this.correctOption = correctOption;
    }

    public int getScore() {
        return this.score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public int getLevel() {
        return this.level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public Question questionText(String questionText) {
        this.questionText = questionText;
        return this;
    }

    public Question options(String[] options) {
        this.options = options;
        return this;
    }

    public Question correctOption(String[] correctOption) {
        this.correctOption = correctOption;
        return this;
    }

    public Question score(int score) {
        this.score = score;
        return this;
    }

    public Question level(int level) {
        this.level = level;
        return this;
    }

    @Override
    public boolean equals(Object o) {
        if (o == this)
            return true;
        if (!(o instanceof Question)) {
            return false;
        }
        Question question = (Question) o;
        return Objects.equals(questionText, question.questionText) && Objects.equals(options, question.options) && Objects.equals(correctOption, question.correctOption) && score == question.score && level == question.level;
    }

    @Override
    public int hashCode() {
        return Objects.hash(questionText, options, correctOption, score, level);
    }

    @Override
    public String toString() {
        return "{" +
            " questionText='" + getQuestionText() + "'" +
            ", options='" + getOptions() + "'" +
            ", correctOption='" + getCorrectOption() + "'" +
            ", score='" + getScore() + "'" +
            ", level='" + getLevel() + "'" +
            "}";
    }

    public static void main(String[] args) {
        
    }
}