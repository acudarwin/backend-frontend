<template>
    <div>
      <h1>Subjects List</h1>
      <SearchBar @onSearch="handleSearch" />
      <button id="new" @click="addSubject">ADD SUBJECT</button>
      <button class="goto" @click="sendStudents">GO TO STUDENTS</button>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="subject in filterData" :key="subject.id">
          <td>{{ subject.name }}</td>
          <td class="actions">
            <button id="edit" @click="editSubject(subject)">Edit</button>
            <button id="delete" @click="deleteById(subject.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
    </div>
  </template>
    
  <script setup>
  import { ref } from "vue"
  import { getSubjects, deleteSubject } from "../api"
  import { useRouter } from "vue-router"
  
  const subjects = ref([])
  const filterData = ref([])
  const router = useRouter()

  const sendStudents = () => {
    router.push({ name: 'students' })
  }

  const addSubject = () => {
    router.push({ name: 'addSubject' })
  };
  
  const editSubject = (subject) => {
    console.log(subject)
    router.push({ name: 'editSubject', params: { id: subject.id } })
  };
  
  const loadSubjects = () => {
    getSubjects().then((response) => {
      subjects.value = response.data
      filterData.value = subjects.value
    });
  };
  
  const handleSearch = (filter) => {
    filterSubjects(filter);
  }
  
  const filterSubjects = ( filter ) => {
    if (filter) {
      filterData.value = subjects.value.filter((subject) => {
        return subject.name.toLowerCase().includes(filter.toLowerCase());
      });
    } else {
      filterData.value = subjects.value;
    }
  }
  
  const deleteById = (id) => {
    deleteSubject(id).then(() => {
      loadSubjects();
    });
  }
  
  loadSubjects();
  </script>
  <style>
  table {
    margin: auto;
    width: 80%;
  }
  th {
    background-color: #4caf50;
    color: white;
  }
  td {
    text-align: left;
    padding: 8px;
  }
  tr:nth-child(even) {
    background-color: #f2f2f2;
  }
  button {
    background-color: #4caf50;
    border: none;
    color: white;
    padding: 10px 16px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
  }
  #edit {
    background-color: #28a745;
    color: #fff;
    border: none;
    border-radius: 0;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 10px 20px;
  }
  
  #edit:hover {
    background-color: #218838;
    color: #fff;
  }
  
  #delete {
    background-color: #dc3545;
    color: #fff;
    border: none;
    border-radius: 0;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 10px 20px;
  }
  
  #delete:hover {
    background-color: #c82333;
    color: #fff;
  }
  
  .actions {
    text-align: center;
  }
  
  .search {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
  }
  </style>