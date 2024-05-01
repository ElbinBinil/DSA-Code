import express, { Request, Response } from "express";
import cors from "cors";
import cookieParser from "cookie-parser";
import { clear } from "console";

export const app = express();

app.use(
  cors({
    origin: process.env.CORS_ORIGIN,
    credentials: true,
  })
);

app.use(express.json({ limit: "16kb" }));
app.use(express.urlencoded({ extended: true, limit: "16kb" }));
app.use(express.static("public"));
app.use(cookieParser());

app.get("/", (req: Request, res: Response) => {
  return res.status(200).json({
    data: "Welcome to backend api!!",
  });
});
