#!/usr/bin/node
const https = require('https');

https.get(process.argv[2], (res) => {
  let data = '';

  res.on('data', (chunk) => {
    data += chunk;
  });

  res.on('end', () => {
    const todos = JSON.parse(data);
    const tasksCompleted = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (!tasksCompleted[todo.userId]) {
          tasksCompleted[todo.userId] = 1;
        } else {
          tasksCompleted[todo.userId]++;
        }
      }
    });

    console.log(tasksCompleted);
  });
}).on('error', (err) => {
  console.error(err);
});      aggregate[element.userId] = 0;
      }
      aggregate[element.userId]++;
    }
  });
  console.log(aggregate);
});
