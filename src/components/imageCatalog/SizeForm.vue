<template>
  <form class="size-form">
    <div v-for="size in $options.sizes"
      :key="size">
      <label :for="size">{{ size }}</label>
      <input type="checkbox"
        :name="size"
        :ref="size"
        :value="inputValues[size]"
        @input="updateSizes()"/>
    </div>
  </form>
</template>

<script>
const sizes = [
  '100%',
  '40px',
  '32px',
  '24px',
  '20px',
  '16px',
  '14px',
  '12px',
  '10px',
];

export default {
  name: 'size-form',
  sizes,
  props: {
    value: {
      type: Array,
      default: () => ['100%'],
    },
  },
  data() {
    return {
      inputValues: {},
    };
  },
  methods: {
    updateSizes() {
      const newInputValues = this.$options.sizes.reduce((obj, size) => {
        const newObj = obj;
        console.log(size);
        const aaa = this.$refs[size];
        const input = this.$refs[size][0];
        console.log(this.$refs[size]);
        console.log(aaa.value);
        console.log(input);
        console.log(input.value);
        newObj[size] = this.$refs[size].value === true;
        return newObj;
      }, {});
      const chosenSizes = this.$options.sizes.filter(size => newInputValues[size]);
      this.inputValues = newInputValues;
      this.$emit('input', chosenSizes);
    },
  },
};
</script>

<style>
</style>
