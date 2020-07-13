const express = require('express')
const fileUpload = require('express-fileupload');
const app = express()
const port = 5000
app.use(fileUpload());

app.post('/upload', function(req, res) {
    // The name of the input field (i.e. "sampleFile") is used to retrieve the uploaded file
    let sampleFile = req.files.sampleFile;
    sampleFile.mv('./test_images/test/1.jpg');
    const { spawn } = require('child_process');
    const pythonProcess = spawn('python',['predict.py']);
    pythonProcess.stdout.on('data', (data) => {
        // Do something with the data returned from python script
        console.log(data.toString().split('\n')[1]);
        res.send(data.toString().split('\n')[1]);
    });
  });


app.listen(port, () => console.log(`Example app listening at http://localhost:${port}`))