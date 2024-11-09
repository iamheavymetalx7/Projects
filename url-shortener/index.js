import express from "express";
const app = express();
import { URL } from "./models/url.js";
import { router as urlRoute } from "./routes/url.js";
import { connectMongoDB } from "./connect.js";
const PORT = 3001;

connectMongoDB("mongodb://localhost:27017/short-url").then(() =>
  console.log("connected to mongoDB")
);
app.use(express.json());

app.use("/url", urlRoute);

app.get("/url/:shortId", async (req, res) => {
  const shortId = req.params.shortId;
  console.log(shortId);
  const entry = await URL.findOneAndUpdate(
    {
      shortId,
    },
    {
      $push: {
        visitHistory: {
          timestamp: Date.now(),
        },
      },
    }
  );
  console.log(entry);
  res.redirect(entry.redirectURL);
});

app.listen(PORT, () => {
  console.log(`server started on ${PORT}`);
});
