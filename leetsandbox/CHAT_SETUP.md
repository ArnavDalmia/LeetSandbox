# ChatGPT Solution Explainer Setup Guide

## Overview
This guide will help you set up the ChatGPT-powered solution explainer feature for your LeetSandbox project.

## Features Implemented
- ✅ Floating chat button on problem pages
- ✅ AI-powered solution explanations with problem context
- ✅ Modern chat UI with overlay
- ✅ Backend API integration with OpenAI
- ✅ Stateless design (no database required)

## Local Development Setup

### 1. Install Dependencies
```bash
cd leetsandbox
pip install -r requirements.txt
```

### 2. Set Up Environment Variables
1. Copy the example environment file:
   ```bash
   cp env.example .env
   ```

2. Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_openai_api_key_here
   ```

3. Get your OpenAI API key from: https://platform.openai.com/api-keys

### 3. Test Locally
1. Start the backend:
   ```bash
   cd leetsandbox
   uvicorn backend.main:app --reload --port 8001
   ```

2. Open your frontend in a browser and navigate to any problem page
3. Click the chat button (💬) in the bottom-right corner
4. Test the chat functionality

## Render Deployment Setup

### 1. Update Render Environment Variables
1. Go to your Render dashboard
2. Select your backend service
3. Go to "Environment" tab
4. Add a new environment variable:
   - **Key**: `OPENAI_API_KEY`
   - **Value**: Your actual OpenAI API key

### 2. Deploy
1. Push your changes to GitHub
2. Render will automatically deploy the updated backend
3. The frontend will be updated via GitHub Pages

## How It Works

### Architecture
```
Frontend (GitHub Pages) → Backend (Render) → OpenAI API
```

### Problem Context
The AI receives full context about the current problem:
- Problem name and LeetCode number
- Parameter types and structure
- LeetCode link for reference
- User's specific question

### Chat Features
- **Stateless**: Each page refresh starts a new chat
- **Context-Aware**: AI knows which problem you're working on
- **Educational**: Provides hints and explanations, not direct solutions
- **Responsive**: Works on desktop and mobile

## API Endpoints

### POST /chat
**Request:**
```json
{
  "problem_slug": "TwoSum",
  "message": "How does the two-pointer approach work?"
}
```

**Response:**
```json
{
  "response": "The two-pointer approach works by...",
  "status": "success"
}
```

## Troubleshooting

### Common Issues

1. **"AI couldn't connect" error**
   - Check if your OpenAI API key is correctly set
   - Verify the backend is running and accessible
   - Check Render logs for errors

2. **Chat button not appearing**
   - Ensure you're on a problem page (not the main page)
   - Check browser console for JavaScript errors

3. **Slow responses**
   - This is expected on Render's free tier (50s cold start)
   - Consider upgrading to a paid plan for instant responses

### Debug Steps
1. Check backend logs in Render dashboard
2. Test the `/chat` endpoint directly with curl:
   ```bash
   curl -X POST "https://your-render-url.onrender.com/chat" \
        -H "Content-Type: application/json" \
        -d '{"problem_slug": "TwoSum", "message": "test"}'
   ```

## Cost Considerations

### OpenAI API Costs
- GPT-4: ~$0.03 per 1K input tokens, ~$0.06 per 1K output tokens
- Typical chat response: ~$0.01-0.05 per message
- Monitor usage in OpenAI dashboard

### Render Costs
- Free tier: 750 hours/month
- Paid tier: $7/month for always-on service

## Next Steps

1. Test the feature thoroughly
2. Monitor API usage and costs
3. Consider adding more problem-specific context
4. Add chat history persistence (optional)
5. Implement rate limiting (if needed)

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review Render and OpenAI logs
3. Test locally first before deploying
