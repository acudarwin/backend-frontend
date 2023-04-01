import axios from 'axios';

const API_URL = 'http://localhost:3000';

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getStudents = () => apiClient.get('/students');

export const getStudent = (id) => apiClient.get(`/students/${id}`);

export const addStudent = (student) => apiClient.post('/students', student);

export const updateStudent = (id, student) => apiClient.put(`/students/${id}`, student);

export const deleteStudent = (id) => apiClient.delete(`/students/${id}`);

export const filterName = (name) => apiClient.get(`/students?firstName=${name}`);


export const getSubjects = () => apiClient.get('/subjects');

export const getSubject = (id) => apiClient.get(`/subjects/${id}`);

export const addSubject = (subject) => apiClient.post('/subjects', subject);

export const updateSubject = (id, subject) => apiClient.put(`/subjects/${id}`, subject);

export const deleteSubject = (id) => apiClient.delete(`/subjects/${id}`);

export const filterSubject = (name) => apiClient.get(`/subjects?name=${name}`);

