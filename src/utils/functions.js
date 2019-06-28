export const importAll = (files) => {
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
};

export const test = () => {};
