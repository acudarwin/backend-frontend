<template>
  <div>
    <h1>Students List</h1>
    <SearchBar @onSearch="handleSearch" />
    <button id="new" @click="addStudent">ADD STUDENT</button>
    <button class="goto" @click="sendSubjects">GO TO SUBJECTS</button>
  <table>
    <thead>
      <tr>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Age</th>
        <th>Email</th>
        <th>Subjects</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="student in filterData" :key="student.id">
        <td>{{ student.firstName }}</td>
        <td>{{ student.lastName }}</td>
        <td>{{ student.age }}</td>
        <td>{{ student.email }}</td>
        <td>
          <ul>
            <li v-for="subject in student.subjects" :key="subject.id">
              {{ subject.name }}
            </li>
          </ul>
        </td>
        <td class="actions">
          <button id="edit" @click="editStudent(student)">Edit</button>
          <button id="delete" @click="deleteById(student.id)">Delete</button>
        </td>
      </tr>
    </tbody>
  </table>
  </div>
</template>
  
<script setup>
import { ref } from "vue"
import { getStudents, deleteStudent, getSubjects } from "../api"
import SearchBar from "./SearchBar.vue"
import { useRouter } from "vue-router"

const students = ref([])
const subjects = ref([])
const filterData = ref([])
const router = useRouter()

const addStudent = () => {
  router.push({ name: 'add' })
};

const sendSubjects = () => {
  router.push({ name: 'subjects' })
}

const editStudent = (student) => {
  console.log(student)
  router.push({ name: 'edit', params: { id: student.id } })
};

const loadStudents = () => {
  getStudents().then((response) => {
    students.value = response.data
    filterData.value = students.value
  });
};

const handleSearch = (filter) => {
  filterStudents(filter);
}

const filterStudents = ( filter ) => {
  if (filter) {
    filterData.value = students.value.filter((student) => {
      return student.firstName.toLowerCase().includes(filter.toLowerCase());
    });
  } else {
    filterData.value = students.value;
  }
}

const deleteById = (id) => {
  deleteStudent(id).then(() => {
    loadStudents();
  });
}

const loadSubjects = () => { 
  getSubjects().then((response) => {
    subjects.value = response.data
    students.value.forEach((student) => {
      student.subjects = subjects.value.filter((subject) => student.subjects.includes(subject.id)); 
      });
    });
  };


loadStudents();
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