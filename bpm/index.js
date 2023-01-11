const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const timestamps = [];

function bpm() {
  if (1 < timestamps.length) {
    return Math.round(60000 / (timestamps.reduce((accum, ts, index) => {
      if (index) {
        return accum + timestamps[ index ] - timestamps[ index - 1 ];
      }
      return accum;
    }, 0) / (timestamps.length - 1)));
  }
  return 0;
}

const handleUserCommand = () => {
  rl.question(`Current BPM: ${bpm()}. Press ENTER rhythmically to update:`, async () => {
    timestamps.push(new Date().getTime());
    while (timestamps.length > 9) {
      timestamps.shift();
    }
    setTimeout(handleUserCommand);
  });
};

handleUserCommand();
