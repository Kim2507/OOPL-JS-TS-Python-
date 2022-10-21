let userID: string[] = ['001','002','003','004','005'];
console.log("Original"+userID);
userID.push('006','007');
console.log("After pushing 2 values " + userID);

console.log("After slicing..."+userID.slice(0,2));