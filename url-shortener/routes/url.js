import express from "express";
import {
  handleGenerateNewURL,
  handleGetAnalytics,
} from "../controllers/index.js";
export const router = express.Router();

router.post("/", handleGenerateNewURL);

router.get("/analytics/:shortId", handleGetAnalytics);
