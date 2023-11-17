```javascript
import axios from 'axios';

const api_instance = axios.create({
  baseURL: 'http://localhost:5000/api',
  timeout: 10000,
  headers: {'Content-Type': 'application/json'}
});

export const processQuery = async (query) => {
  try {
    const response = await api_instance.post('/process_query', { query });
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const transactionProcessing = async (transactionData) => {
  try {
    const response = await api_instance.post('/transaction_processing', transactionData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const walletManagement = async (walletData) => {
  try {
    const response = await api_instance.post('/wallet_management', walletData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const smartContractInteraction = async (contractData) => {
  try {
    const response = await api_instance.post('/smart_contract_interaction', contractData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const contextUnderstanding = async (contextData) => {
  try {
    const response = await api_instance.post('/context_understanding', contextData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const sentimentAnalysis = async (sentimentData) => {
  try {
    const response = await api_instance.post('/sentiment_analysis', sentimentData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
```