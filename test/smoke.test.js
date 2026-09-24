const express=require('express');const z=require('zod');
const app=express();
const S=z.object({id:z.string()});
if(!S.safeParse({id:'a'}).success){process.exit(1)}
console.log('smoke ok');
