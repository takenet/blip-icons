<template>
  <div class="image-catalog">
    <div id="desk-svg-browser">
      <p>Desk SVG files</p>
      <div id="svg-browser" class="image-browser">
        <svg-container
          v-for="(svg, index) in $options.svgLibrary.desk"
          v-once
          :key="index"
          :originalPath="svg.originalPath"
          :path="svg.path"/>
      </div>
    </div>

    <div id="portal-svg-browser">
      <p>Portal SVG files</p>
      <div id="svg-browser" class="image-browser">
        <svg-container
          v-for="(svg, index) in $options.svgLibrary.portal"
          v-once
          :key="index"
          :originalPath="svg.originalPath"
          :path="svg.path"/>
      </div>
    </div>
  </div>
</template>

<script>
import SvgContainer from './SvgContainer.vue';

function importAll(files) {
  const keys = files.keys();
  const pathMap = keys.map(files);
  return keys.map(
    (key, index) => {
      const path = pathMap[index];
      return {
        originalPath: key,
        path,
      };
    },
  );
}

const deskSvgFiles = importAll(require.context('../../assets/img/organized-new/desk/3-compressed', true, /\.svg$/));
const portalSvgFiles = importAll(require.context('../../assets/img/organized-new/portal/all', true, /\.svg$/));


const svgLibrary = {
  desk: [
    ...new Set(deskSvgFiles),
  ],
  portal: [
    ...new Set(portalSvgFiles),
  ],
};

export default {
  name: 'new-image-catalog',
  svgLibrary,
  components: {
    SvgContainer,
  },
};
</script>

<style>
</style>
