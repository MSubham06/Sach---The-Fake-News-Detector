* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
  background-color: #f5f5f5;
  color: #333;
  line-height: 1.6;
}

.app {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

header {
  text-align: center;
  margin-bottom: 30px;
}

header h1 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.news-form {
  background: white;
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 30px;
}

.news-form textarea {
  width: 100%;
  min-height: 150px;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
  margin-bottom: 15px;
  resize: vertical;
}

.news-form button {
  background-color: #3498db;
  color: white;
  border: none;
  padding: 12px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.news-form button:hover {
  background-color: #2980b9;
}

.news-form button:disabled {
  background-color: #95a5a6;
  cursor: not-allowed;
}

.result {
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 20px;
  background: white;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.result.real {
  border-left: 5px solid #2ecc71;
}

.result.fake {
  border-left: 5px solid #e74c3c;
}

.result h3 {
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.confidence {
  font-weight: bold;
  margin: 10px 0;
}

.tips {
  margin-top: 15px;
  padding-top: 15px;
  border-top: 1px solid #eee;
}

.tips h4 {
  margin-bottom: 10px;
}

.tips ul {
  padding-left: 20px;
}

.tips li {
  margin-bottom: 5px;
}

.error {
  color: #e74c3c;
  padding: 15px;
  background: #fadbd8;
  border-radius: 4px;
  margin-bottom: 20px;
}

footer {
  margin-top: auto;
  text-align: center;
  padding: 20px;
  color: #7f8c8d;
  font-size: 14px;
}

@media (max-width: 600px) {
  .app {
    padding: 15px;
  }
  
  .news-form {
    padding: 15px;
  }
}
