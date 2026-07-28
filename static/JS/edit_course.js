const questionsList = document.getElementById("questions");
const addButton = document.getElementById("add");
const saveButton = document.getElementById("save-edit");
const saveState = document.getElementById("save-state");
const courseInfo = document.getElementById("course-info");
const editorShell = document.querySelector(".editor-shell");
const storageKey = `course-edit:${editorShell ? editorShell.dataset.courseId : "new"}`;
let questions = 0;

function createField(type, index, value = "") {
    const field = document.createElement("div");
    const label = document.createElement("label");
    const input = document.createElement("input");
    const id = `${type}${index}`;

    field.className = "field";
    label.setAttribute("for", id);
    label.textContent = type === "question" ? "Question" : "Answer";
    input.id = id;
    input.type = "text";
    input.name = id;
    input.dataset.type = type;
    input.placeholder = type === "question" ? "Enter question" : "Enter answer";
    input.value = value;

    field.append(label, input);
    return field;
}

function setSaveState(text) {
    if (saveState) {
        saveState.textContent = text;
    }
}

function getRowsData() {
    return [...questionsList.querySelectorAll(".question-row")].map((row) => ({
        question: row.querySelector('[data-type="question"]').value,
        answer: row.querySelector('[data-type="answer"]').value
    }));
}

function createQuestionRow(question = "", answer = "") {
    questions += 1;

    const row = document.createElement("div");
    const removeButton = document.createElement("button");

    row.className = "question-row";
    removeButton.className = "icon-button question-delete";
    removeButton.type = "button";
    removeButton.setAttribute("aria-label", "Delete question");
    removeButton.textContent = "×";
    removeButton.addEventListener("click", function () {
        row.remove();
        if (!questionsList.querySelector(".question-row")) {
            questionsList.append(createQuestionRow());
        }
        setSaveState("Unsaved changes");
    });

    row.append(createField("question", questions, question), createField("answer", questions, answer), removeButton);
    return row;
}

function loadEdit() {
    let saved = null;

    try {
        saved = JSON.parse(localStorage.getItem(storageKey) || "null");
    } catch {
        saved = null;
    }

    const savedQuestions = saved && Array.isArray(saved.questions) ? saved.questions : [];

    if (saved && courseInfo) {
        courseInfo.value = saved.info || "";
    }

    questionsList.replaceChildren();

    if (savedQuestions.length) {
        savedQuestions.forEach((item) => {
            questionsList.append(createQuestionRow(item.question || "", item.answer || ""));
        });
    } else {
        questionsList.append(createQuestionRow());
    }
}

if (questionsList && addButton) {
    loadEdit();

    addButton.addEventListener("click", function () {
        questionsList.append(createQuestionRow());
        setSaveState("Unsaved changes");
    });
}
document.addEventListener("input", function (event) {
    if (event.target.closest(".editor-shell")) {
        setSaveState("Unsaved changes");
    }
});
saveButton.addEventListener("click", async ()=>{
    let questions2=[]
    for(let i=1;i<=questions;i+=1){
        let question=document.getElementById("question"+i)
        let answer=document.getElementById("answer"+i)
        if(question){
            questions2.push([question.value,answer.value])
        }
    }
    let course={
        "theory_text":courseInfo.value,
        "questions":questions2,
        "course_id":editorShell.dataset.courseId
    }
    let serverResponse=await fetch("/save",{
        method:"POST",
        headers:{
            "content-type":"application/json"
        },
        body:JSON.stringify(course)
    })
})