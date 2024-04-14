var read=require('readline-sync')
num1=read.question('enter 2 numbers ')
num2=read.question('')

if(num1>num2){
    console.log('greater is ' +num1)
} else{
    console.log('greater is ' +num2)
}