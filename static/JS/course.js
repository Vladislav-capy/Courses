let submit=document.getElementById("submit")
let answers=document.getElementsByClassName("ans")

submit.addEventListener("click",async function(){
    let counter=0
    for(let i of answers){
        
        if(i.value===""){
            i.style.borderColor="red"
            i.placeholder="Enter answer"
            i.classList.add("error")
            counter=counter+1
            return
        }
        if(i.value.trim()===""){
            i.style.borderColor="red"
            i.placeholder="Enter answer"
            i.classList.add("error")
            counter=counter+1
            return
        }
        
    }
    let anss=[]
    for(let i of answers)
    {
        anss.push(i.value)
    }
    if(counter===0){
        let serverResponse=await fetch("/check_answers",{
            "method":"POST",
            "headers":{
                "content-type":"application/json"
            },
            "body":JSON.stringify(anss)
        })
    if(serverResponse.ok){
        console.log(serverResponse)
        return
    }
    else{
        alert("Something went wrong...")
    }
        }
})