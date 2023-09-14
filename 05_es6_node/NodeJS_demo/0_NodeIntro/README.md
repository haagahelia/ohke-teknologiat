# Creating Node.js backend with TypeScript, Express, Knex

## Create a git repo for your project

Go to GitHub.com ,to your own account and create a new repo 'ts-node-app'.
- Create the repo private for the time being.
- Add README.md
- Use gitignore template: Node 

- clone the repo to some local folder on your computer 
(Note: repo cannot be inside another repo folder, nor its subfolders)

----

## Install Node.js if you don't have it yet

(Installing node installs npm and npx too)

## Make the repo folder become a node project

> npm init -y   

(y = yes to everything, don't ask for options)

creates the **package.json** file:   (removed some extra things)
```
{
  "name": "ts-node-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "repository": {
    "type": "git",
    "url": "git+https://github.com/valju/ts-node-app.git"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

More info when needed: https://docs.npmjs.com/cli/v10/configuring-npm/package-json 


## package.json file modifications - ES module support

We want to be able to use ES modules (import/export) instead of the old CommonJS module system (require/module.exports). ((( Though you can set old CommonJS files to work too in settings, and then import some from './olderCode.cjs'  . Notice the .cjs file extension )))

package.json addition:
```
"type":"module", 
```

in .ts code files later
```
import some, {other, third as fourth} from './xyz.js';

// Here 'default import' some and two 'named imports' other and third (third renamed as fourth for our code file)

// Note that file extension .js might be reuired for your own codefiles, depending on settings.
// And its not the .ts but the output .js
```


This is how we would install typescript modules to node project, so that it they will be used only during development time, but not in the built Production version (js, html, css etc. only):

## Changing project to TypeScript
> npm install typescript --save-dev 

package.json addition:
```
"devDependencies": {
   "typescript":"^4.9.7"
}
```

> npx tsc --init

That created the tsconfig.json file. Let's modify it to look like this:

### tsconfig.json

Some of the interesting ones set to what we want below. (More info if needed: https://www.typescriptlang.org/tsconfig)
```
{
   "compilerOptions": {
     "target": "ES2020", 
     "module": "es2020",
     "moduleResolution": "node",
     "sourceMap": true,
     "outDir": "dist",

     "esModuleInterop":true,
     "strict": true,
     "skipLibCheck" : true,
     "forceConsistentCasingInFileNames": true,
   },
   "include":["src/**/*"],
}
```
And let's also create the src folder that we remember to put our code there. Output dir 'dist' will be created automatically.

## Writing scripts taking care of TypeScript compilation and build deployment

Let's install a helper module rimraf for removing (rm) folder (r) recursively and (f) forcibly 

> npm install -D rimraf               

That refers to the unix command: rm -rf

Then we are ready to edit new scripts in **package.json** for running and building the node app that we write in TypeScript:
```
"scripts": {
   "build":"rimraf dist && npx tsc",
   "prestart":"npm run build",
   "start":"node dist/index.js",
   "preserve":"npm run build",
   "serve": "npx tsc -w & nodemon dist/index.js" 
}
```

The & in scripts means both are started parallel. And && would mean consecutive, second one only started when first script has finished. 

These come from unix/linux terminal. But they require terminal that supports such terminal syntax. To do the same more multi-platform way we can install node module called concurrently:

> npm install concurrently

In package.json scripts we utilize concurrently and give it two scripts to run concurrently. On console they would be surrounded by " which is problem in JSON, as it would break the JSON file structure. Thus escape character \" has to be used four times inside that JSON string:

```
   "serve": "concurrently  \"npx tsc -w\"   \"nodemon dist/index.js\" "
```

## Making the project a Node.js backend with Express

> npm install express knex mysql 

> npm i -D @types/express  @types/node

> npm run build 

> npm run serve

index.ts:

```  
import express, {Express, Request, Response } from "express";

const app: Express = express();
const port: number = 3333;

app.listen(port, () => {
    console.log(`now listening on port ${port}`);
})
```

Then let's start copying, from the following project: https://github.com/haagahelia/Siba_be,

Here is the src/index.js first: Change the file to this, and start giving the missing parts, or comment out initially:


```
import express, {Express} from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import dotenv from 'dotenv';

import logger from './utils/logger.js';
import routes from './routes/index.js';

const app:Express = express();
const port:number = 3335;
dotenv.config({});  // Reads the .env values from disk

app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.json());
app.use(`/api`, routes );


app.listen(port, () => {
  console.log(`Backend starting on port ${port}`);
  logger.log('info', `Backend starting on port ${port}`);
});
```

Comment out all lines causing problems first. Then add e.g. the logger and test. Then add routing index from below. Each time comment out what is not implemented yet.

> npm run serve


Then file by file copy following folder and named file, and make it work for our case:
(= remove extras that are not there yet or won't be at all)
- src/utils/logger.js    (ready-made, don't edit, just use)
- src/routes/index.js    (need to edit based on the removed/added routes)
- src/responseHandlers/index.js    (ready-made, don't edit, just use)
- src/validationHandler/index.js    (ready-made common parts, remove extras, edit/add needed)
- src/types        (edit where needed)
- src/routes/building.ts  (Remove so far all related to DB, db_knex, authenticator, admin, statist, planner. Put some fake data returned) 

# Task this week
1. Follow the lesson recording on how to make the backend to work for one route to work (no DB yet, no authentication or roles) and tested.
1. You might need to install more modules, e.g. module with types for MySQLError or such.
1. Using same model, add there src/routes/category.ts   (Category will have id -number and name -string, and optional description -longer string). Make three fake Category routes of your choice. GET, GET (all), POST, PUT, DELETE. (Later they can be made to be real knex+mariadb routes). Make some programming logic, e.g. could 
check that the POSTed Category's name does not exist already, and that PUTted Category's id exists. Or some other programming you can then test.
1. Create some validators for the routes, using the existing models
1. Create a PDF containing src/routes/index.ts src/routes/category.ts src/validationHandler/*.ts  AND some PostMan screens (request & data, result)
**Note:** You most likely don't need to edit root index, logger, responseHandlers, validate function or so common parts. Only building parts while doing the demo, and then only category related parts.

# TypeScript - What TypeScript features will we use?
- parameter type, return type, assignment type checking / enforcing
- member and parameter auto-complete/intellisense while writing the code
- interface for request body or URL parameter validators
- more?

https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html

# What other things to learn here?
- Express routing for backend
- Express validators
- Express middleware function idea   (req, resp, next()) in the request handling chain
- Logger