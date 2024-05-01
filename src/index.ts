import { app } from "./app";

import dotenv from "dotenv";

dotenv.config({
  path: "./.env",
});

try {
  app.listen(process.env.PORT || 3001, () => {
    console.log(`Server is running on the port ${process.env.PORT}`);
  });
} catch {
  (error: any) => {
    console.log("Connection error ..", error);
  };
}
