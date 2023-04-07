const { SlippiGame } = require("@slippi/slippi-js");
const fs = require('fs');
const slp = process.argv[2]
const game = new SlippiGame(slp);

// // Get game settings – stage, characters, etc
// const settings = game.getSettings();
// console.log(settings);

// // Get metadata - start time, platform played on, etc
// const metadata = game.getMetadata();
// console.log(metadata);

// Get computed stats - openings / kill, conversions, etc


const stats = game.getStats();
const combos = stats.combos;
console.log('@ALL COMBOS@\n');
for (let key in combos){
	console.log('@COMBO START@\n');
	console.log(combos[key]);
	console.log("\n@COMBO END@\n");
}





// Get frames – animation state, inputs, etc
// This is used to compute your own stats or get more frame-specific info (advanced)
// const frames = game.getFrames();
// console.log(frames[0].players); // Print frame when timer starts counting down