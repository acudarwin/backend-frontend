<template>
    <div>
      <form @submit.prevent="saveSubject">
        <label>Name</label>
        <input v-model="subject.name" required/>
        <button class="save" type="submit">Save</button>
        <button class="cancel" type="button" @click="cancelEdit">Cancel</button>
      </form>
    </div>
</template>
  
<script setup>
  import { useRouter } from "vue-router"
  import { ref } from "vue"
  import { addSubject, getSubject, updateSubject } from '../api';

  const router = useRouter()
  const { id } = router.currentRoute.value.params

  const subject= ref({
    name: ''
  })

  const loadSubject = (id) => {
    console.log('[id]', id);
    if (id) {
      getSubject(id).then((response) => {
        subject.value = response.data;
      });
    }
  };

  loadSubject(id);

  const saveSubject = () => {

    if (!id) {
      addSubject(subject.value).then(() => {
        router.push({ name: 'subjects' });
      });
      return;
    } else {
      updateSubject(id, subject.value).then(() => {
        router.push({ name: 'subjects' });
      });
    }
  };

  const cancelEdit = () => {
    router.push({ name: 'subjects' });
  };
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
</style>