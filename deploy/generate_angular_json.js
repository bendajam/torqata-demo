const fs = require('fs');
const path = require('path');


console.log('POST BUILD SCRIPT STARTED');
const statsPath = path.join(process.cwd(), '/app/static/stats.json');
const manifestPath = path.join(process.cwd(), '/app/static/manifest.json')
const stats = require(statsPath)

fs.writeFileSync(manifestPath, JSON.stringify(stats["assetsByChunkName"]));

console.log('POST BUILD SCRIPT FINISHED');