let div=document.getElementById("questions")
let button=document.getElementById("add")
let questions=0
let elements=0
for(let i of div.children){
    elements=elements+1
}
questions=elements/2
button.addEventListener("click",function(){
    questions=questions+1
    div.innerHTML+=`<input type="text" name="question${questions}"> <input type="text" name="answer${questions}"></input>`
})