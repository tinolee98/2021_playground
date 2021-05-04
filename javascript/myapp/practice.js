var userID = 1;
var userName = 'Lee';
var result = 1+2; 
var user = { id:1, name: 'Lee'};
var users = [
    {id:1, name: 'Lee'},
    {id :2, name: 'Kim'}
];

console.log("ab" + "asdf" + "asdf");


var expression = 1;

switch (expression) {
    case 1:
        console.log(`${expression}, ${typeof expression}`);
        //만약 break가 없다면.
    case 10:
        console.log("case 10");
        break;
    default:
        console.log("default");
}

foo: {
    console.log("foo");
    break foo;
    console.log("somebody helpme!"); // 어차피 없는 친구다 이말이야.
}
console.log("I'm out")

outer: for(var i=0;i<3;i++){
    inner:for(var j=0;j<3;j++){
        if (i+j === 3) break inner;
        console.log(`i ${i}, j ${j}`);
    }
}
console.log("done!");
console.log(Array+'');

function add(x,y) {
    console.log(arguments);
    return x+y;
}

add(2,5,10);
