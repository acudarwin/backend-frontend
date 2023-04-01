<template>
    <div>
      <form @submit.prevent="saveStudent">
        <label>FirstName</label>
        <input v-model="student.firstName" required/>
        <label>LastName</label>
        <input v-model="student.lastName" required/>
        <label>Age</label>
        <input v-model="student.age" required/>
        <label>Email</label>
        <input v-model="student.email" required/>
        <label>Subjects</label>
        <select class="my-select" v-model="student.subjects" multiple>
          <option v-for="subject in subjects" :value="subject.id" :key="subject.id">{{ subject.name }}</option>
        </select><br>
        <button class="save" type="submit">Save</button>
        <button class="cancel" type="button" @click="cancelEdit">Cancel</button>
      </form>
    </div>
</template>
  
<script setup>
  import { useRouter } from "vue-router"
  import { ref } from "vue"
  import { addStudent, getStudent, updateStudent, getSubjects } from '../api';

  const router = useRouter()
  const { id } = router.currentRoute.value.params
  const subjects = ref([]);

  const student= ref({
    firstName: '',
    lastName: '',
    age: '',
    email: '',
    subjects: [],
  })

  const loadStudent = (id) => {
    console.log('[id]', id);
    if (id) {
      getStudent(id).then((response) => {
        student.value = response.data;
      });
    }
  };
  
  const loadSubjects = () => { 
  getSubjects().then((response) => {
    subjects.value = response.data;
  });
  };
    loadStudent(id);

  const saveStudent = () => {

    if (!id) {
      addStudent(student.value).then(() => {
        router.push({ name: 'students' });
      });
      return;
    } else {
      updateStudent(id, student.value).then(() => {
        router.push({ name: 'students' });
      });
    }
  };

  const cancelEdit = () => {
    router.push({ name: 'students' });
  };

  loadSubjects();
</script>
<style scoped>
  button {
    background-color: #4caf50;
    border: none;
    color: white;
    padding: 10px 16px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
  }
  input {
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
  }
  label {
    padding: 12px 20px;
    margin: 8px 0;
    box-sizing: border-box;
  }
  .save {
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 0;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 10px 20px;
  }
  
  .save:hover {
    background-color: #0069d9;
    color: #fff;
  }

  .cancel {
    background-color: #6c757d;
    color: #fff;
    border: none;
    border-radius: 0;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 10px 20px;
  }
  
  .cancel:hover {
    background-color: #5a6268;
    color: #fff;
  }

  .my-select {
    background-color: #f5f5f5;
    border: none;
    color: #333;
    padding: 10px;
    font-size: 16px;
    border-radius: 5px;
    width: 100%;
    max-width: 400px;
    height: 80px;
    cursor: pointer;
    position: relative;
  }

  .my-select:focus {
    outline: none;
  }

  .my-select option {
    background-color: #fff;
    color: #333;
    font-size: 16px;
    cursor: pointer;
  }

  .my-select option:hover {
    background-color: #e6e6e6;
  }

  .my-select option:checked {
    background-color: #d9edf7;
    color: #333;
    font-weight: bold;
  }

  .my-select option:checked:hover {
    background-color: #c4e3f3;
  }

  .my-select::after {
    content: "\f078";
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    pointer-events: none;
  }

  @font-face {
    font-family: "Font Awesome 5 Free";
    src: url("https://use.fontawesome.com/releases/v5.15.3/webfonts/fa-solid-900.woff2") format("woff2");
    font-weight: 900;
    font-style: normal;
    font-display: block;
  }
</style>