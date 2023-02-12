console.log("Inside my script.js");
function showAlert() { window.alert(`loaded!`) };

function changeHeaderToRed() {
    let elem = document.getElementById('my-header');
    elem.style.color = 'red';
}

function switchColor(className) {
    const elements = document.getElementsByClassName(className)
    for (let index = 0; index < elements.length; index++) {
        const element = elements[index]
        let currClass = null
        newClass = null
        if (element.classList.contains('btn-primary')) {
            currClass = 'btn-primary'
            newClass = 'btn-danger'
        } else {
            currClass = 'btn-danger'
            newClass = 'btn-primary'
        }
        element.classList.replace(currClass, newClass)
    }
    let btn = document.getElementById('color-change')
    if (btn.classList.contains('btn-danger')) {
        btn.innerText = 'Change elements to Blue'
    } else {
        btn.innerText = 'Change elements to Red'
    }
}