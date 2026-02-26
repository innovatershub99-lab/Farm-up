# Farm-up

This repository contains the FarmUp Next.js application. I fixed build issues related to Tailwind and TypeScript event handlers so the project builds successfully.

How to run locally

1. Install dependencies

```powershell
cd farmup
npm ci
```

2. Run development server

```powershell
npm run dev
```

3. Build for production

```powershell
npm run build
npm start
```

Notes
- This project uses Next.js (app directory) and TailwindCSS.
- If Vercel is connected to this repo, pushing to `main` will trigger a redeploy automatically.

If you want, I can add GitHub Actions or detailed deployment steps for Vercel.
# FarmUp - AI-Powered Farming Assistant 🌱

## Overview

FarmUp is a comprehensive AI-powered farming assistant designed to help farmers make informed decisions about crop planting, monitoring, and harvesting. The application provides intelligent crop recommendations, real-time weather monitoring, market price insights, and includes multilingual support with voice control capabilities.

## 🚀 Features

### Core Features
- **User Authentication & Onboarding**: Simple login/registration system with demo credentials
- **AI-Powered Crop Recommendations**: Intelligent suggestions based on soil conditions, weather, and market trends
- **Real-time Weather Monitoring**: Current weather conditions and forecasts with alerts
- **Market Price Insights**: Live market prices and trends for various crops
- **Crop Monitoring Dashboard**: Track crop growth, health status, and progress throughout the lifecycle

### Advanced Features
- **Voice Control**: Voice commands for hands-free interaction (Web Speech API)
- **Multilingual Support**: Available in English, Hindi, Spanish, and French
- **Video Tutorials**: Comprehensive farming technique videos categorized by topic
- **Mobile-Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Data Visualization**: Interactive charts and progress tracking
- **Real-time Notifications**: Toast notifications for user feedback and alerts

## 🛠 Technology Stack

- **Frontend**: HTML5, CSS3 (Tailwind CSS), Vanilla JavaScript
- **Styling**: Tailwind CSS with custom color palette
- **Icons**: Heroicons (SVG)
- **APIs**: Web Speech API for voice control
- **Storage**: LocalStorage for demo data persistence
- **Server**: Python HTTP server for development

## 📱 Application Structure

```
farmup/
├── public/
│   ├── index.html          # Landing page with authentication
│   ├── dashboard.html      # Main dashboard
│   ├── tutorials.html      # Video tutorials page
│   ├── monitoring.html     # Crop monitoring page
│   └── app.js             # Core JavaScript functionality
├── src/
│   ├── app/               # Next.js app structure (for TypeScript setup)
│   ├── components/        # React components (for reference)
│   ├── lib/              # Utility libraries
│   ├── types/            # TypeScript type definitions
│   └── data/             # JSON data files
├── server.py             # Development server
└── README.md
```

## 🎯 Key Pages

### 1. Landing Page (`/`)
- Hero section with FarmUp branding
- Login/Registration forms with demo credentials
- Feature preview cards
- Responsive design with animations

### 2. Dashboard (`/dashboard.html`)
- Weather monitoring with current conditions
- Crop recommendations with suitability scores
- Market prices with trend indicators
- Voice assistant integration
- Quick action buttons

### 3. Video Tutorials (`/tutorials.html`)
- Categorized farming videos
- Filter by topic (planting, irrigation, harvesting, pest control)
- Video cards with thumbnails and descriptions
- Difficulty levels and duration indicators

### 4. Crop Monitoring (`/monitoring.html`)
- Active crop tracking
- Growth progress visualization
- Health status monitoring
- Add new crops functionality
- Notes and observations system

## 🎮 Demo Credentials

**Email**: demo@farmup.com  
**Password**: demo123

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Modern web browser with JavaScript enabled

### Installation & Setup

1. **Navigate to the project directory**:
   ```bash
   cd farmup
   ```

2. **Start the development server**:
   ```bash
   python server.py
   ```

3. **Open your browser** and navigate to `http://localhost:8000`

4. **Login** using the demo credentials or create a new account

## 📖 Usage Guide

### Authentication
1. Use demo credentials (demo@farmup.com / demo123) for quick access
2. Or register a new account with any email and password
3. Authentication state is preserved in localStorage

### Dashboard Navigation
- **Weather Section**: View current conditions and alerts
- **Crop Recommendations**: See AI-suggested crops with suitability scores
- **Market Prices**: Check current market trends
- **Voice Assistant**: Click the microphone to use voice commands

### Voice Commands
Try these voice commands:
- "What crops should I plant?"
- "Check weather forecast"
- "Show market prices"
- "Weather information"

### Adding Crops
1. Go to Crop Monitoring page
2. Click "Add New Crop"
3. Fill in crop details (name, size, planting date, location)
4. Track progress and add notes as crops grow

### Video Learning
1. Browse tutorials by category
2. Filter by planting, irrigation, harvesting, or pest control
3. View difficulty levels and video duration
4. Click play to start learning

## 🌟 Features in Detail

### AI Crop Recommendations
- Analyzes soil conditions, weather patterns, and market trends
- Provides suitability scores (0-100%)
- Shows expected yield and current market prices
- Considers seasonal factors and crop rotation

### Weather Integration
- Real-time weather data display
- Temperature, humidity, wind speed monitoring
- Weather alerts for farming decisions
- Forecast information for planning

### Market Intelligence
- Current crop prices with currency
- Price change indicators (rising/falling/stable)
- Percentage change calculations
- Market trend analysis

### Voice Control
- Natural language processing for farming queries
- Hands-free operation for field use
- Multi-language voice recognition
- Context-aware responses

### Multilingual Support
- English (default)
- Hindi (हिंदी)
- Spanish (Español)
- French (Français)
- Easy language switching in header

## 🎨 Design System

### Color Palette
- **Primary Green**: #16a34a (farming/nature theme)
- **Secondary Colors**: Blue (#3b82f6), Yellow (#eab308), Red (#ef4444)
- **Neutral Grays**: Various shades for text and backgrounds

### Typography
- **Font**: Inter (Google Fonts)
- **Headings**: Bold, hierarchical sizing
- **Body Text**: Regular weight, high readability

### Components
- **Cards**: White background with subtle shadows
- **Buttons**: Primary (green) and secondary (gray) variants
- **Forms**: Clean inputs with focus states
- **Progress Bars**: Visual progress indicators
- **Toast Notifications**: Contextual feedback system

## 📊 Sample Data

The application includes comprehensive sample data:
- **6 crop varieties** with detailed specifications
- **Mock weather data** for demonstration
- **Market prices** with realistic fluctuations
- **Crop monitoring records** with various growth stages
- **Video tutorials** across different farming topics

## 🔧 Customization

### Adding New Crops
Edit `/src/data/crops.json` to add new crop varieties with:
- Scientific names and categories
- Soil and climate requirements
- Growth duration and yield expectations
- Market price information

### Modifying UI Theme
Update Tailwind configuration in HTML files:
```javascript
tailwind.config = {
  theme: {
    extend: {
      colors: {
        primary: {
          // Custom color palette
        }
      }
    }
  }
}
```

## 🚀 Production Deployment

For production deployment:

1. **Static Hosting**: Deploy the `public/` folder to any static hosting service
2. **Environment Variables**: Replace mock data with real API endpoints
3. **Authentication**: Integrate with Firebase or similar service
4. **APIs**: Connect to real weather and market price APIs
5. **Database**: Replace localStorage with proper database storage

## 🤝 Contributing

This is a hackathon prototype designed to demonstrate AI-powered farming solutions. The application showcases:
- Modern web development practices
- Responsive design principles
- Accessibility considerations
- User experience optimization

## 📱 Browser Support

- **Chrome/Chromium**: Full support including voice features
- **Firefox**: Full support with voice features
- **Safari**: Full support (voice features may vary)
- **Edge**: Full support including voice features
- **Mobile Browsers**: Responsive design works on all modern mobile browsers

## 🔐 Security Notes

This is a demo application with:
- Mock authentication (localStorage-based)
- No real user data collection
- Client-side only implementation
- No external API calls (all data is mocked)

## 📈 Future Enhancements

Potential improvements for production:
- **IoT Integration**: Connect with soil sensors and weather stations
- **Satellite Imagery**: Crop health monitoring from space
- **Machine Learning**: Improved crop recommendations with historical data
- **Mobile App**: Native iOS/Android applications
- **Blockchain**: Supply chain tracking and verification
- **AI Chatbot**: Advanced conversational interface
- **Drone Integration**: Aerial crop monitoring and spraying
- **Financial Integration**: Crop insurance and loan services

## 📞 Support

This is a hackathon prototype. For questions or improvements, refer to the documentation above or examine the well-commented source code.

---

**Built with ❤️ for modern farmers using AI and web technologies** 🌾🚀