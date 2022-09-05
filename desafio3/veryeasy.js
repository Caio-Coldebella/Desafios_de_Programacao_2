const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("", (answer) => {
  if(answer === null){
    rl.close()
  }
  console.log(answer)
});