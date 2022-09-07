// for(let v =0 ; v<20; v=v+1)
// {
   
// var a = document.querySelector('.comparison1')[v]
// var b = document.querySelector('.comparison2')

// a.style.backgroundColor = 'green';

// }

var ele1 = document.getElementsByClassName('comparison1');
var ele2 = document.getElementsByClassName('comparison2');
var purchase = document.getElementsByClassName('purchase');
var sno = document.getElementsByClassName('sno');
var cap = document.getElementsByClassName('capitalise');
console.log("length is : ", ele1.length)
for (var i = 0; i < ele1.length; i++ ) {
    value1 = parseFloat(ele1[i].textContent)
    value2 = parseFloat(ele2[i].textContent)
    value3 = parseFloat(purchase[i].textContent)
    if (value1 > value2)
    {
        ele1[i].style.backgroundColor = 'green';
        ele2[i].style.backgroundColor = 'red';

    }
    else if(value1 < value2)
    {
        ele2[i].style.backgroundColor = 'green';
        ele1[i].style.backgroundColor = 'red';
    }

    if(value2<value3)
    {
        purchase[i].style.backgroundColor = 'red';
    }

    // also adding Sno.
    sno[i].textContent = i+1;

    // capitalise
    // console.log("\n\n",cap[i].textContent.toUpperCase(), "\n\n")
    cap[i].textContent = cap[i].textContent.toUpperCase()
    
    // textAlign

    ele1[i].style.textAlign = 'center';
    ele2[i].style.textAlign = 'center';
    purchase[i].style.textAlign = 'center';
}