const express = require('express');
const app = express();

const notes = [];

app.post('/notes', (req, res) => {
  const { idEstudiante, notaEstudiante } = req.body;
  notes.push({ idEstudiante, notaEstudiante });
  res.send('Note created successfully');
});

app.get('/notes/:idEstudiante', (req, res) => {
  const idEstudiante = req.params.idEstudiante;
  const note = notes.find(n => n.idEstudiante === idEstudiante);
  if (note) {
    res.json(note);
  } else {
    res.status(404).send('Note not found');
  }
});

app.listen(8081, () => {
  console.log('Notes service is running on port 8081');
});