# NOTE: We install application dependencies into a different directory
# from the application directory to avoid an issue reported in https://stackoverflow.com/q/30043872.
# This workaround is also described in https://stackoverflow.com/a/35317425.
FROM node:17

CMD ["node", "app.js"]

# Set the working directory to the directory for the installed dependencies.
WORKDIR /authlete/install

# Copy package.json and package-lock.json.
COPY package*.json ./

# Set NODE_ENV.
# NOTE: If NODE_ENV is set to 'production', 'npm ci' command doesn't
# install devDependencies.
ARG NODE_ENV
ENV NODE_ENV $NODE_ENV

# Install dependencies based on package-lock.json.
RUN npm ci && npm cache clean --force

# Set NODE_PATH. The application loads the dependencies from this path.
ENV NODE_PATH=/authlete/install/node_modules

# Set the working directory to the application directory.
WORKDIR /authlete/app

# Copy the application files.
COPY . .