properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/avielb/DevOps0909.git"
    }
    stage("show files"){
         bat "dir"
    }
}
